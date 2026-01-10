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


class MailboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mailbox"

    @property
    def original_file_name(self) -> "str":
        return "mailbox.svg"

    @property
    def title(self) -> "str":
        return "mailbox"

    @property
    def primary_color(self) -> "str":
        return "#ABE659"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>mailbox</title>
     <path d="m14.196
 20.014-7.711-5.836c-.48-.31-.733-.268-1.121.155a71.39 71.39 0 0
 0-.26.303c-.226.275-.353.451-.262.775.007.043 2.397 7.352 2.397
 7.352.225.782.782 1.212 1.642 1.226h3.545c.543 0 .825-.112
 1.142-.479l.966-1.283c.67-.951.592-1.459-.338-2.22m-10.22-5.8L9.81
 6.494c.31-.48.268-.733-.155-1.12-.105-.092-.204-.177-.303-.261-.275-.226-.45-.353-.775-.261-.042.007-7.352
 2.396-7.352 2.396C.444 7.475.014 8.032 0 8.892v3.545c0
 .543.113.825.48 1.142l1.282.965c.952.67 1.46.593
 2.22-.338m16.043-4.412-5.836 7.71c-.31.48-.268.734.155
 1.122l.303.26c.275.226.45.353.775.261.042-.007 7.352-2.396
 7.352-2.396.782-.226 1.212-.783
 1.226-1.643v-3.545c0-.543-.113-.825-.48-1.142l-1.282-.965c-.952-.67-1.46-.593-2.22.338M9.79
 3.986l7.711 5.836c.48.31.733.268
 1.121-.155l.26-.303c.226-.275.353-.451.262-.775-.007-.043-2.397-7.352-2.397-7.352-.225-.782-.782-1.212-1.642-1.226h-3.546c-.542
 0-.824.112-1.141.479l-.966 1.283c-.67.951-.592 1.459.338 2.22" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
