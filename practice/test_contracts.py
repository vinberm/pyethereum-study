# -*- coding: utf8 -*-
from os import path
import pytest

from rlp.utils import encode_hex

from ethereum import tester
from ethereum import utils
from ethereum import _solidity
from ethereum._solidity import get_solidity

SOLIDITY_AVAILABLE = get_solidity() is not None
CONTRACTS_DIR = path.join(path.dirname(__file__), 'contracts')


@pytest.mark.skipif(not SOLIDITY_AVAILABLE, reason='solc compiler not available')
def test_library_from_file():
    state = tester.state()
    state.env.config['HOMESTEAD_FORK_BLKNUM'] = 0  # enable CALLCODE opcode

    library = state.abi_contract(
        None,
        path=path.join(CONTRACTS_DIR, 'seven_library.sol'),
        language='solidity',
    )

    libraries = {
        'SevenLibrary': encode_hex(library.address),
    }
    contract = state.abi_contract(
        None,
        path=path.join(CONTRACTS_DIR, 'seven_contract.sol'),
        libraries=libraries,
        language='solidity',
    )

    # pylint: disable=no-member
    assert library.seven() == 7
    assert contract.test() == 7



@pytest.mark.skipif(not SOLIDITY_AVAILABLE, reason='solc compiler not available')
def test_library_from_code():
    with open(path.join(CONTRACTS_DIR, 'seven_library.sol')) as handler:
        library_code = handler.read()

    with open(path.join(CONTRACTS_DIR, 'seven_contract_without_import.sol')) as handler:
        contract_code = handler.read()

    state = tester.state()
    state.env.config['HOMESTEAD_FORK_BLKNUM'] = 0  # enable CALLCODE opcode

    library = state.abi_contract(
        library_code,
        path=None,
        language='solidity',
    )

    libraries = {
        'SevenLibrary': encode_hex(library.address),
    }
    contract = state.abi_contract(
        contract_code,
        path=None,
        libraries=libraries,
        language='solidity',
    )

    # pylint: disable=no-member
    assert library.seven() == 7
    assert contract.test() == 7