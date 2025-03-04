"""
Python equivalent of js-source/important-modifier.test.ts
Last synced with original version: Current (as of implementation)

This test file maintains exact parity with the TypeScript tests to ensure
consistent behavior between the JavaScript and Python implementations.

This test file verifies the functionality of important modifiers (both `!` suffix and `!` prefix styles).
"""

import pytest
from tw_merge import tw_merge


def test_merges_tailwind_classes_with_important_modifier_correctly():
    """Test that Tailwind classes with important modifiers merge correctly."""
    # Latest Tailwind CSS v3 syntax (! suffix)
    assert tw_merge('font-medium! font-bold!') == 'font-bold!'
    assert tw_merge('font-medium! font-bold! font-thin') == 'font-bold! font-thin'
    assert tw_merge('right-2! -inset-x-px!') == '-inset-x-px!'
    assert tw_merge('focus:inline! focus:block!') == 'focus:block!'
    assert tw_merge('[--my-var:20px]! [--my-var:30px]!') == '[--my-var:30px]!'
    
    # Tailwind CSS v3 legacy syntax
    assert tw_merge('font-medium! !font-bold') == '!font-bold'
    
    assert tw_merge('!font-medium !font-bold') == '!font-bold'
    assert tw_merge('!font-medium !font-bold font-thin') == '!font-bold font-thin'
    assert tw_merge('!right-2 !-inset-x-px') == '!-inset-x-px'
    assert tw_merge('focus:!inline focus:!block') == 'focus:!block'
    assert tw_merge('![--my-var:20px] ![--my-var:30px]') == '![--my-var:30px]' 