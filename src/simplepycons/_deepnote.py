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


class DeepnoteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deepnote"

    @property
    def original_file_name(self) -> "str":
        return "deepnote.svg"

    @property
    def title(self) -> "str":
        return "Deepnote"

    @property
    def primary_color(self) -> "str":
        return "#3793EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deepnote</title>
     <path d="M10.22
 11.506l.111.018c-.038-.006-.075-.011-.111-.018zm4.475
 8.073c.636-2.816-2.172-4.8-6.955-4.814L.713
 24h9.586c.132-.025.256-.056.384-.085 2.258-1.057 3.598-2.501
 4.012-4.336zM10.299 24h.203l.021-.01c-.075.003-.148.008-.224.01zM24
 11.319C24 3.15 18.711-.597 8.134.077L0 11.319h7.568c3.323 0 8.457.719
 8.457 6.153 0 3.622-1.909 5.798-5.727
 6.528.099-.003.194-.009.291-.013l-.011.001-.076.012h.912l.247-.077C19.885
 23.27 24 19.07 24 11.319z" />
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
