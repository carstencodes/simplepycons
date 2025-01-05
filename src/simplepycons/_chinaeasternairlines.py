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


class ChinaEasternAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chinaeasternairlines"

    @property
    def original_file_name(self) -> "str":
        return "chinaeasternairlines.svg"

    @property
    def title(self) -> "str":
        return "China Eastern Airlines"

    @property
    def primary_color(self) -> "str":
        return "#1A2477"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>China Eastern Airlines</title>
     <path d="M11.572 2.383c-1.846 0-2.245.238-2.962
 1.205-.38.516-3.568 4.915-5.009
 6.898-.18.236-.446.486-1.03.486H0v.004c3.05 8.61 6.324 10.64 9.602
 10.64h5.178c.07 0
 .146-.08-.041-.124-3.805-.953-7.57-3.984-7.589-6.962.066 2.464 5.255
 3.315 10.876
 4.016.098.011.093-.065.063-.12l-.17-.293c-.02-.039-.043-.068-.124-.088-3.094-.787-6.242-1.938-6.242-3.01
 0-2.032 5.272-4.042
 11.27-4.96.195-.04.29-.076.42-.18.17-.136.536-.433.695-.554.096-.085.061-.11.025-.11-.16
 0-.326.004-.485.01-7.898.219-15.544 2.008-16.253
 4.55-.002.014-.01.027-.014.04.937-4.652 7.198-9.162
 15.008-11.28.18-.052.239-.168.014-.168Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://uk.ceair.com/newCMS/uk/en/content/en_'''

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
