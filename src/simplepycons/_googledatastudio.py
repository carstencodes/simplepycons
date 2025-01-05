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


class GoogleDataStudioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googledatastudio"

    @property
    def original_file_name(self) -> "str":
        return "googledatastudio.svg"

    @property
    def title(self) -> "str":
        return "Google Data Studio"

    @property
    def primary_color(self) -> "str":
        return "#669DF6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Data Studio</title>
     <path d="M19.197 23.002c-1.016-.613-1.697-1.728-1.697-3
 0-1.273.681-2.388 1.697-3h-6.909a3.034 3.034 0 0 0-.252-.011c-1.656
 0-3.022 1.355-3.036 3.011v.014c0 1.645 1.354 3 3 3 .096 0
 .192-.005.288-.014h6.909Zm1.803-6c1.656 0 3 1.344 3 3s-1.344 3-3
 3-3-1.344-3-3 1.344-3
 3-3Zm-10.803-2.004c-1.016-.613-1.697-1.728-1.697-3 0-1.273.681-2.388
 1.697-3H3.288a3.034 3.034 0 0 0-.252-.011C1.38 8.987.014 10.342 0
 11.998v.014c0 1.645 1.354 3 3 3 .096 0
 .192-.005.288-.014h6.909Zm1.803-6c1.656 0 3 1.344 3 3s-1.344 3-3
 3-3-1.344-3-3 1.344-3
 3-3Zm7.197-2.004c-1.016-.613-1.697-1.728-1.697-3 0-1.273.681-2.388
 1.697-3h-6.909c-.08-.006-.16-.01-.24-.01C10.39.984 9.021 2.336 9
 3.994v.014c0 1.645 1.354 3 3 3 .096 0
 .192-.005.288-.014h6.909Zm1.803-6c1.656 0 3 1.344 3 3s-1.344 3-3
 3-3-1.344-3-3 1.344-3 3-3Z" />
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
