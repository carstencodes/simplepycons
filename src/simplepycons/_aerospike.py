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


class AerospikeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aerospike"

    @property
    def original_file_name(self) -> "str":
        return "aerospike.svg"

    @property
    def title(self) -> "str":
        return "Aerospike"

    @property
    def primary_color(self) -> "str":
        return "#C22127"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Aerospike</title>
     <path d="M14.347 15.375 7.45 12.283l6.897-3.072v6.164zM24
 0v24H0V0h24zm-4.705 5.386L5.672 11.548l-1.607.743 1.607.688 13.623
 6.163v-1.565l-3.576-1.602V8.612l3.576-1.586v-1.64z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://pages.aerospike.com/rs/aerospike/imag'''

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
