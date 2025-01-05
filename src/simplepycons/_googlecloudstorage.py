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


class GoogleCloudStorageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecloudstorage"

    @property
    def original_file_name(self) -> "str":
        return "googlecloudstorage.svg"

    @property
    def title(self) -> "str":
        return "Google Cloud Storage"

    @property
    def primary_color(self) -> "str":
        return "#AECBFA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Cloud Storage</title>
     <path d="M24 2.4v8.4h-2.4V2.4H24zM0
 10.8h2.4V2.4H0v8.4zm3-8.4h18v8.4H3V2.4zm12.6 4.2a1.8 1.8 0 1 0 3.6 0
 1.8 1.8 0 0 0-3.6 0zm-10.8.6H12V6H4.8v1.2zm16.8
 14.4H24v-8.4h-2.4v8.4zM0
 21.6h2.4v-8.4H0v8.4zm3-8.4h18v8.4H3v-8.4zm12.6 4.2a1.8 1.8 0 1 0 3.6
 0 1.8 1.8 0 0 0-3.6 0zM4.8 18H12v-1.2H4.8V18z" />
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
