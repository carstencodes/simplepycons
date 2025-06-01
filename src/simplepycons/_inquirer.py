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


class InquirerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "inquirer"

    @property
    def original_file_name(self) -> "str":
        return "inquirer.svg"

    @property
    def title(self) -> "str":
        return "Inquirer"

    @property
    def primary_color(self) -> "str":
        return "#F0DB4F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Inquirer</title>
     <path d="M8.132
 7.14v-.99h.992v-.992h5.752v.992h.793v.991h.992v2.777h-.992v.992h-.793v.992h-.992v.992h-.991v2.975h-1.786V12.1h.992v-.992h.992v-.991h.992v-.992h.991v-1.19h-.991v-.992H9.917v.992h-.991v1.983H7.14V7.14Zm-2.578-.198H1.587v10.116h3.967v1.785H0V5.157h5.554zm12.892
 0h3.967v10.116h-3.967v1.785H24V5.157h-5.554zm-7.339
 10.116h1.786v1.785h-1.786z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/SBoudrias/Inquirer.js/blob'''

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
