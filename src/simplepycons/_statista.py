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


class StatistaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "statista"

    @property
    def original_file_name(self) -> "str":
        return "statista.svg"

    @property
    def title(self) -> "str":
        return "Statista"

    @property
    def primary_color(self) -> "str":
        return "#001327"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Statista</title>
     <path d="M.8597 0a.84.84 0 0
 0-.8404.8404v15.2165H.14s3.6114-.0681 5.1428-.8739a10.89 10.89 0 0 0
 3.337-3.0513l.903-1.2746.2857-.4062c.0343-.04.1821-.2571.2678-.3828s.4581-.6506.8181-1.1764a16.94
 16.94 0 0 1 5.2623-4.7433c3.3371-1.7142 7.76-1.5424
 7.76-1.5424h.0681V.8917A.84.84 0 0 0 23.1455 0Zm23.1195 7.9487a.9.9 0
 0 1-.2166.029s-3.6054.068-5.154.8794a10.86 10.86 0 0 0-3.3382
 3.0458l-.885 1.2801c-.1314.1829-.257.3652-.2913.4052l-.269.3828-.817
 1.1774s-2.1776 3.1433-5.2633 4.7433c-3.2 1.6629-7.3882 1.5539-7.731
 1.5425v1.7142A.84.84 0 0 0 .8541 24h22.2857a.84.84 0 0 0
 .8393-.8404z" />
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
