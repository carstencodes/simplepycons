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


class StackeditIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stackedit"

    @property
    def original_file_name(self) -> "str":
        return "stackedit.svg"

    @property
    def title(self) -> "str":
        return "StackEdit"

    @property
    def primary_color(self) -> "str":
        return "#606060"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>StackEdit</title>
     <path d="M6 0C2.689 0 0 2.689 0 6v12c0 3.311 2.689 6 6 6h12c3.311
 0 6-2.689 6-6V6c0-3.311-2.689-6-6-6H6zm.227 1.871h11.546A3.98 3.98 0
 0 1 21.75 5.85v11.545a3.978 3.978 0 0 1-3.977 3.976H6.227a3.978 3.978
 0 0 1-3.977-3.976V5.85a3.98 3.98 0 0 1 3.977-3.98zm-.223
 2.31V6.01H4.633V7.7h1.37v1.903h-1.37v1.689h1.37v1.828h1.4v-1.828h1.695v1.828h1.398v-1.828h1.371v-1.69h-1.37v-1.9h1.37V6.01h-1.37V4.182h-1.4V6.01H7.403V4.182H6.004zm1.398
 3.52h1.696v1.903H7.402V7.7z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/benweet/stackedit/blob/463'''

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
