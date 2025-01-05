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


class CleverCloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clevercloud"

    @property
    def original_file_name(self) -> "str":
        return "clevercloud.svg"

    @property
    def title(self) -> "str":
        return "Clever Cloud"

    @property
    def primary_color(self) -> "str":
        return "#171C36"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Clever Cloud</title>
     <path d="M4.823 11.139 11.253 0 1.608 5.57zM1.235
 6.646v10.708L4.325 12zM12 23.57l6.43-11.14H5.57zM12 .43 5.57
 11.57h12.86zm10.764 16.924V6.646L19.674
 12zm.001.862-.374.215-3.215-5.57L12.746 24zm0-12.431L12.745 0l6.431
 11.139 3.215-5.57zM1.235 18.216 11.254 24l-6.43-11.138-3.216 5.569z"
 />
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
