#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class MessengerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "messenger"

    @property
    def original_file_name(self) -> "str":
        return "messenger.svg"

    @property
    def title(self) -> "str":
        return "Messenger"

    @property
    def primary_color(self) -> "str":
        return "#0866FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Messenger</title>
     <path d="M12 0C5.24 0 0 4.952 0 11.64c0 3.499 1.434 6.521 3.769
 8.61a.96.96 0 0 1 .323.683l.065 2.135a.96.96 0 0 0
 1.347.85l2.381-1.053a.96.96 0 0 1 .641-.046A13 13 0 0 0 12 23.28c6.76
 0 12-4.952 12-11.64S18.76 0 12 0m6.806 7.44c.522-.03.971.567.63
 1.094l-4.178 6.457a.707.707 0 0 1-.977.208l-3.87-2.504a.44.44 0 0
 0-.49.007l-4.363
 3.01c-.637.438-1.415-.317-.995-.966l4.179-6.457a.706.706 0 0 1
 .977-.21l3.87 2.505c.15.097.344.094.491-.007l4.362-3.008a.7.7 0 0 1
 .364-.13" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://about.meta.com/brand/resources/facebo'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://about.meta.com/brand/resources/facebo'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
