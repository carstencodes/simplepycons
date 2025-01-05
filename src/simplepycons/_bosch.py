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


class BoschIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bosch"

    @property
    def original_file_name(self) -> "str":
        return "bosch.svg"

    @property
    def title(self) -> "str":
        return "Bosch"

    @property
    def primary_color(self) -> "str":
        return "#EA0016"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bosch</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12C23.996 5.374 18.626.004 12 0zm0 22.88C5.991 22.88 1.12 18.009
 1.12 12S5.991 1.12 12 1.12 22.88 5.991 22.88 12c-.006 6.006-4.874
 10.874-10.88 10.88zm4.954-18.374h-.821v4.108h-8.24V4.506h-.847a8.978
 8.978 0 0 0 0 14.988h.846v-4.108h8.24v4.108h.822a8.978 8.978 0 0 0
 0-14.988zM6.747 17.876a7.86 7.86 0 0 1
 0-11.752v11.752zm9.386-3.635h-8.24V9.734h8.24v4.507zm1.12
 3.61V6.124a7.882 7.882 0 0 1 0 11.727z" />
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
