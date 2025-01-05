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


class DpdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dpd"

    @property
    def original_file_name(self) -> "str":
        return "dpd.svg"

    @property
    def title(self) -> "str":
        return "DPD"

    @property
    def primary_color(self) -> "str":
        return "#DC0032"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DPD</title>
     <path d="M16.01 10.71a.364.364 0 01-.343-.006l-.558-.331a.43.43 0
 01-.182-.312l-.014-.65a.363.363 0
 01.165-.3l6.7-3.902L12.377.085A.799.799 0 0012 0a.798.798 0
 00-.377.085l-9.4 5.124 10.53 6.13c.098.054.172.181.172.295v8.944c0
 .112-.08.241-.178.294l-.567.315c-.171.062-.256.043-.361
 0l-.569-.315a.362.362 0 01-.175-.294v-7.973a.223.223 0
 00-.095-.156L1.702 7.048v10.579c0 .236.167.528.371.648l9.556
 5.636c.102.06.237.09.371.089a.745.745 0
 00.371-.09l9.557-5.635a.835.835 0 00.37-.648V7.047Z" />
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
