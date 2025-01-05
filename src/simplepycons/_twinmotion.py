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


class TwinmotionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "twinmotion"

    @property
    def original_file_name(self) -> "str":
        return "twinmotion.svg"

    @property
    def title(self) -> "str":
        return "Twinmotion"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Twinmotion</title>
     <path d="M12 .1175C7.08.1175 2.8508 3.0792.9994
 7.3172h15.7994v.0045l-2.364 16.5475C19.8947 22.7444 24 17.9096 24
 12.1175h-6.261l.6875-4.8003h4.5741C21.1484 3.0784 16.9208.1175 12
 .1175m-12 12c0 5.8163 4.1393 10.666 9.6331 11.765l1.681-11.765Z" />
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
