#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class LubuntuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lubuntu"

    @property
    def original_file_name(self) -> "str":
        return "lubuntu.svg"

    @property
    def title(self) -> "str":
        return "Lubuntu"

    @property
    def primary_color(self) -> "str":
        return "#0068C8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lubuntu</title>
     <path d="M12 0C5.373 0 .001 5.374.001 12.001c0
 .154.003.307.009.46 3.832-2.705 10.368-7.163 11.987-7.28.537-.68
 2.37-1.22 2.704-1.209l-.957 1.198s-.03 1.224-.388 1.462c3.34 2.233
 4.944 10.262 5.626 15.126A11.98 11.98 0 0024 12.001C24 5.374 18.629 0
 12 0zm-.593 10.842c-.899.027-2.743 2.712-4.825 5.588-1.001
 1.382-2.035 2.823-2.988 4.134A11.96 11.96 0 0012 24c2.347 0
 4.537-.672 6.386-1.837-1.423-4.35-4.128-11.299-6.897-11.315a.394.394
 0 00-.082-.006zM4.679 11.94c-.823-.007-2.86.701-4.607 1.375.178
 1.632.681 3.166 1.447 4.535.35-.53.716-1.077 1.08-1.61 1.386-2.038
 2.729-3.838 2.413-4.21-.056-.062-.171-.09-.333-.09zm2.165
 1.025c-.664.1-3.064 3.09-4.97 5.478.31.487.653.948 1.028 1.384
 1.96-3.21 4.153-6.707 4.035-6.851a.16.16 0 00-.093-.011Z" />
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
