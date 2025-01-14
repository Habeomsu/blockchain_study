'''지갑 wallet 거래 담당 기능 구현'''
import hashlib
import codecs
import base58
from ecdsa import NIST256p, SigningKey


class Wallet:
    '''코인 전자지갑'''
    def __init__(self) -> None:
        '''객체 생성할 때 초기화'''
        self._private_key = SigningKey.generate(curve=NIST256p)
        self._public_key = self._private_key.get_verifying_key()
        self._blockchain_address = self.generate_blockchain_address()
        

    @property
    def blockchain_address(self) -> str:
        '''생성된 지갑 주소 리턴'''
        return self._blockchain_address

    @property
    def private_key(self) -> str:
        '''Private key를 문자열로 변환하여 리턴'''
        return self._private_key.to_string().hex()

    @property
    def public_key(self) -> str:
        '''public key를 문자열로 변환하여 리턴'''
        return self._public_key.to_string().hex()

    def generate_blockchain_address(self) -> str:
        '''블록체인(지갑) 주소 생성'''
        # Step 1. private/public key 생성 -> __init__ 에서 이미 생성(생략)
        # Step 2. Public key에 SHA-256 수행
        public_key_bytes = self._public_key.to_string()
        sha256_bpk = hashlib.sha256(public_key_bytes)
        sha256_bpk_digest = sha256_bpk.digest()

        # Step 3. SHA-256 수행 결과에 RipeMD160 수행
        ripemd160_bpk = hashlib.new('ripemd160')
        ripemd160_bpk.update(sha256_bpk_digest)
        ripemd160_bpk_digest = ripemd160_bpk.digest()
        ripemd160_bpk_digest_hex = codecs.encode(ripemd160_bpk_digest,'hex')

        # Step 4. Network byte 추가
        network_coin_public_key = b'00' + ripemd160_bpk_digest_hex
        network_coin_public_key_bytes = codecs.decode(
            network_coin_public_key,
            'hex'
        )

        # Step 5. SHA-256 2회 수행
        sha256_bpk_digest = hashlib.sha256(network_coin_public_key_bytes).digest()
        sha256_2_bpk_digest = hashlib.sha256(sha256_bpk_digest).digest()
        sha256_hex = codecs.encode(sha256_2_bpk_digest,'hex')

        # Step 6. Checksum 구하기
        checksum = sha256_hex[:8]

        # Step 7. Public Key에 Checksum 더하기
        addr_hex = (sha256_hex + checksum).decode('utf-8')
        
        # Step 8. 더한 키를 Base58로 인코딩
        blockchain_addr = base58.b58encode(addr_hex).decode('utf-8')
        return blockchain_addr


    def generate_signature(
            self,
    ) -> str:
        '''거래에 필요한 signature생성'''

    def calculate_total_amount(self,) -> float:
         '''blockchain_addr에 해당하는 계좌 총액을 리턴'''

