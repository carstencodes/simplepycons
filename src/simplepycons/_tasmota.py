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


class TasmotaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tasmota"

    @property
    def original_file_name(self) -> "str":
        return "tasmota.svg"

    @property
    def title(self) -> "str":
        return "Tasmota"

    @property
    def primary_color(self) -> "str":
        return "#1FA3EC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tasmota</title>
     <path d="M12 0L0 12l1.371 1.372L12 2.743l10.629 10.629L24 12 12
 0zm0 8.463a7.41 7.41 0 0 0-2.64 14.334v-2.133a5.464 5.464 0 0 1
 1.671-10.17V24h1.94V10.494a5.464 5.464 0 0 1 1.669 10.171v2.133A7.41
 7.41 0 0 0 12 8.463z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tasmota/docs/blob/f9ad7161'''

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
