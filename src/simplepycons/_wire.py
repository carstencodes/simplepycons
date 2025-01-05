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


class WireIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wire"

    @property
    def original_file_name(self) -> "str":
        return "wire.svg"

    @property
    def title(self) -> "str":
        return "Wire"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wire</title>
     <path d="M24 14.475c.009 4.084-3.296 7.401-7.38
 7.41h-.016c-1.637-.015-3.222-.58-4.5-1.605-3.269 2.544-7.981
 1.957-10.524-1.313-1-1.286-1.555-2.862-1.58-4.492V2.82h1.41v11.655c-.002
 3.314 2.683 6.002 5.996 6.004 1.293.001 2.552-.416
 3.589-1.189-1.163-1.335-1.806-3.043-1.815-4.814v-9.54c0-1.557
 1.263-2.82 2.82-2.82s2.82 1.263 2.82 2.82v9.54c.006 1.766-.623
 3.474-1.77 4.814 2.674 1.957 6.429 1.371 8.383-1.304.745-1.019
 1.149-2.248
 1.157-3.511V2.82H24v11.655zm-10.59-9.54c0-.778-.632-1.41-1.41-1.41-.779
 0-1.41.631-1.41 1.41v9.54c.002 1.41.501 2.776 1.41 3.855.908-1.079
 1.408-2.445 1.41-3.855v-9.54z" />
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
