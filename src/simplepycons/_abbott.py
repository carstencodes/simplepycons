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


class AbbottIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "abbott"

    @property
    def original_file_name(self) -> "str":
        return "abbott.svg"

    @property
    def title(self) -> "str":
        return "Abbott"

    @property
    def primary_color(self) -> "str":
        return "#008FC7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Abbott</title>
     <path d="M20.812 2.4H0v3.197h19.773V5.6a1.03 1.03 0 0 1 1.032
 1.031v10.742l-.004.007a1.034 1.034 0 0 1-1.034 1.025H4.23c-.569
 0-1.033-.46-1.033-1.033v-4.34c0-.57.464-1.032
 1.033-1.032H17.6V8.803H3.188A3.185 3.185 0 0 0 0 11.99v6.423A3.188
 3.188 0 0 0 3.188 21.6h17.624A3.187 3.187 0 0 0 24 18.412V5.587A3.186
 3.186 0 0 0 20.812 2.4" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Logo_'''

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
