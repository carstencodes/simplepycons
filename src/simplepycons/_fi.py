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


class FiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fi"

    @property
    def original_file_name(self) -> "str":
        return "fi.svg"

    @property
    def title(self) -> "str":
        return "Fi"

    @property
    def primary_color(self) -> "str":
        return "#00B899"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fi</title>
     <path d="M14.908 4.621c0-1.749 1.472-3.162 3.286-3.162 1.813 0
 3.287 1.416 3.287 3.162s-1.472 3.162-3.287 3.162c-1.816
 0-3.286-1.414-3.286-3.162zM24 17.077h-.735c-1.507
 0-2.267-1.069-2.267-2.753v-3.162h-5.569v4.482c0 4.869 3.228 6.913
 6.353 6.913H24ZM5.578 18.581c0-1.628.901-2.369
 2.731-2.369h4.541v-5.064H5.578V9.057c0-1.654 1.427-2.552
 3.132-2.552h4.133V1.443H7.289C2.925 1.443 0 3.753 0
 8.594v13.95h5.578Z" />
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
        yield from [
            "epiFi",
            "Fi.Money",
        ]
