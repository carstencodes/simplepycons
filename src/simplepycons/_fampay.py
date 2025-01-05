#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
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


class FampayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fampay"

    @property
    def original_file_name(self) -> "str":
        return "fampay.svg"

    @property
    def title(self) -> "str":
        return "FamPay"

    @property
    def primary_color(self) -> "str":
        return "#FFAD00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FamPay</title>
     <path d="M14.828 23.971a.206.206 0
 01-.233-.016c-.646-.407-3.892-2.571-6.089-5.288-1.34-1.677
 3.783-4.173 3.783-3.844.005 1.782.5 6.467 2.603 8.747a.268.268 0
 01-.013.356l-.051.035 M13.48 13.082l4.659-2.119a4.386 4.386 0
 002.542-2.636l.581-1.634a.174.174 0 00-.11-.222.171.171 0 00-.125
 0l-8.897 3.771.033-.142a.902.902 0 01.439-.626c1.505-.927 6.903-3.686
 6.903-3.686a6.592 6.592 0 003.53-4.112L23.444.28a.225.225 0
 00-.153-.268.222.222 0 00-.144 0s-8.123 3.156-10.734 4.425C9.8 5.707
 7.126 7.34 6.2 12.142c-.376 1.945.313 3.592 1.607 5.46-.006-1.836
 4.637-4.02 5.673-4.52z M2.026 4.86C1.289 4.299.662 4.25.553
 4.299c-.049-.174.846-.597.956-.707.362-.346.565-.804.988-1.098.863-.611
 1.93-.424 2.824.064.455.25 1.709 1.071 1.728 1.112A14.02 14.02 0
 018.945 5.38a.241.241 0 010 .314c-.211.203-.418.348-.675.565-1.703
 1.43-2.73 5.24-2.746 5.711V12s-.999-5.38-3.498-7.14z" />
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
