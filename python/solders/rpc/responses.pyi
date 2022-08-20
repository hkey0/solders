from __future__ import annotations
from typing import Sequence, List, Optional, TypeVar, Union, Tuple, Dict
from solders.hash import Hash
from solders.account import Account, AccountJSON
from solders.transaction_status import (
    EncodedTransactionWithStatusMeta,
    Reward,
)
from solders.signature import Signature
from solders.pubkey import Pubkey
from solders.transaction import VersionedTransaction

class RpcResponseContext:
    slot: int
    api_version: Optional[str]
    def __init__(self, slot: int, api_version: Optional[str] = None) -> None: ...

class RpcError:
    code: int
    message: str
    def __init__(self, code: int, message: str) -> None: ...

T = TypeVar("T")
Resp = Union[RpcError, T]

class GetAccountInfoResp:
    context: RpcResponseContext
    value: Optional[Account]
    def __init__(
        self, value: Optional[Account], context: RpcResponseContext
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetAccountInfoResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetAccountInfoResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetAccountInfoJsonParsedResp:
    context: RpcResponseContext
    value: Optional[AccountJSON]
    def __init__(
        self, value: Optional[AccountJSON], context: RpcResponseContext
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetAccountInfoJsonParsedResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetAccountInfoJsonParsedResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBalanceResp:
    context: RpcResponseContext
    value: int
    def __init__(self, value: int, context: RpcResponseContext) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBalanceResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBalanceResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockCommitmentResp:
    commitment: Optional[List[int]]
    total_stake: int
    def __init__(
        self, commitment: Optional[Sequence[int]], total_stake: int
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockCommitmentResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockCommitmentResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockHeightResp:
    def __init__(self, height: int) -> None: ...
    @property
    def height(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockHeightResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockHeightResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class RpcBlockProductionRange:
    def __init__(
        self,
        first_slot: int,
        last_slot: int,
    ) -> None: ...
    @property
    def first_slot(self) -> int: ...
    @property
    def last_slot(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> RpcBlockProductionRange: ...
    @staticmethod
    def from_bytes(data: bytes) -> RpcBlockProductionRange: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class RpcBlockProduction:
    def __init__(
        self,
        by_identity: Dict[Pubkey, Tuple[int, int]],
        range: RpcBlockProductionRange,
    ) -> None: ...
    @property
    def by_identity(self) -> Dict[Pubkey, Tuple[int, int]]: ...
    @property
    def range(self) -> RpcBlockProductionRange: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> RpcBlockProduction: ...
    @staticmethod
    def from_bytes(data: bytes) -> RpcBlockProduction: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockProductionResp:
    value: RpcBlockProduction
    context: RpcResponseContext
    def __init__(
        self, value: RpcBlockProduction, context: RpcResponseContext
    ) -> None: ...
    @property
    def height(self) -> int: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockProductionResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockProductionResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockResp:
    previous_blockhash: Hash
    blockhash: Hash
    parent_slot: int
    transactions: Optional[List[EncodedTransactionWithStatusMeta]]
    signatures: Optional[List[Signature]]
    rewards: Optional[List[Reward]]
    block_time: Optional[int]
    block_height: Optional[int]
    def __init__(
        self,
        previous_blockhash: Hash,
        blockhash: Hash,
        parent_slot: int,
        transactions: Optional[Sequence[EncodedTransactionWithStatusMeta]] = None,
        signatures: Optional[Sequence[Signature]] = None,
        rewards: Optional[Sequence[Reward]] = None,
        block_time: Optional[int] = None,
        block_height: Optional[int] = None,
    ) -> None: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlocksResp:
    def __init__(self, blocks: List[int]) -> None: ...
    @property
    def blocks(self) -> List[int]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlocksResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlocksResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...

class GetBlockTimeResp:
    def __init__(self, time: Optional[int] = None) -> None: ...
    @property
    def time(self) -> Optional[int]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> Resp[GetBlockTimeResp]: ...
    @staticmethod
    def from_bytes(data: bytes) -> GetBlockTimeResp: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...
