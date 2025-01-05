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


class OpenprojectIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openproject"

    @property
    def original_file_name(self) -> "str":
        return "openproject.svg"

    @property
    def title(self) -> "str":
        return "OpenProject"

    @property
    def primary_color(self) -> "str":
        return "#0770B8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenProject</title>
     <path d="M19.35.37h-1.86a4.628 4.628 0 0 0-4.652
 4.624v5.609H4.652A4.628 4.628 0 0 0 0 15.23v3.721c0 2.569 2.083 4.679
 4.652 4.679h1.86c2.57 0 4.652-2.11 4.652-4.679v-3.72c0-.063
 0-.158-.005-.158H8.373v3.88c0 1.026-.835 1.886-1.861
 1.886h-1.86c-1.027 0-1.861-.864-1.861-1.886V15.23a1.839 1.839 0 0 1
 1.86-1.833h14.697c2.57 0 4.652-2.11 4.652-4.679V4.997A4.628 4.628 0 0
 0 19.35.37Zm1.861 8.345c0 1.026-.835 1.886-1.861
 1.886h-3.721V4.997a1.839 1.839 0 0 1 1.86-1.833h1.86a1.839 1.839 0 0
 1 1.862 1.833zm-8.373 9.706a.236.236 0 0 0 0 .03c0 .746.629 1.344
 1.396 1.344.767 0 1.395-.594 1.395-1.34a.188.188 0 0 0
 0-.034v-3.35h-2.791z" />
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
