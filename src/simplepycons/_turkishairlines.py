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


class TurkishAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "turkishairlines"

    @property
    def original_file_name(self) -> "str":
        return "turkishairlines.svg"

    @property
    def title(self) -> "str":
        return "Turkish Airlines"

    @property
    def primary_color(self) -> "str":
        return "#C70A0C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Turkish Airlines</title>
     <path d="M.168 13.988c.272 1.623.86 3.115 1.69 4.423 3.095-.863
 5.817-2.495 6.785-6.132 1.065-4.003-.15-8.199-3.057-10.422C1.626
 4.364-.657 9.077.168 13.988m23.664-3.975c1.098 6.534-3.308
 12.722-9.844 13.819-1.1.185-2.19.214-3.245.103a12.023 12.023 0 0
 1-8.46-4.892l19.428-5.57c.279-.08.207-.349-.024-.333l-8.145.569c1.148-1.108
 2.021-2.467 1.915-4.345-.214-3.043-3.311-6.013-9.071-7.967a12.016
 12.016 0 0 1 6.87-1.333c5.228.548 9.663 4.512 10.576 9.95" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.turkishairlines.com/en-int/press-'''

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
