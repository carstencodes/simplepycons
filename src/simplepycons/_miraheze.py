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


class MirahezeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "miraheze"

    @property
    def original_file_name(self) -> "str":
        return "miraheze.svg"

    @property
    def title(self) -> "str":
        return "Miraheze"

    @property
    def primary_color(self) -> "str":
        return "#FFFC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Miraheze</title>
     <path d="m2.677 12.923 3.768.011 1.949 3.369-1.926
 3.323H2.666L.727 16.292l1.95-3.369Zm-.004-8.6 3.761.011 1.944
 3.367-1.922 3.326H2.662L.727 7.69l1.946-3.367Zm14.882 0 3.768.011
 1.95 3.367-1.928 3.326h-3.801L15.606 7.69l1.949-3.367Zm0 8.6
 3.768.011 1.95 3.369-1.928 3.323h-3.802l-1.937-3.334
 1.949-3.369Zm-7.456 4.373 3.767.011 1.951 3.368L13.889
 24h-3.801l-1.939-3.336 1.95-3.368Zm0-17.296 3.767.011 1.951
 3.369-1.928 3.324h-3.801L8.149 3.368 10.099 0Zm0 8.628 3.767.011
 1.951 3.368-1.928 3.325h-3.801l-1.939-3.336 1.95-3.368Z" />
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
