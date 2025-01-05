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


class ZaimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zaim"

    @property
    def original_file_name(self) -> "str":
        return "zaim.svg"

    @property
    def title(self) -> "str":
        return "Zaim"

    @property
    def primary_color(self) -> "str":
        return "#50A135"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zaim</title>
     <path d="M7.748.453C6.13.453 4.852.623 4
 1.047c-.51.255-1.191.765-1.446 1.784-.256 1.019.17 1.782.51
 2.122a8.258 8.258 0 0 0 2.212 1.613c-1.872.425-3.404.933-4.255
 1.528C.512 8.434 0 9.028 0 10.13v9.426c0 1.104.51 1.697.936 2.037
 1.533 1.103 5.449 1.953 9.96 1.953 4.513 0 8.429-.765
 9.961-1.953.511-.34 1.022-.933 1.022-2.037v-9.426c0-.17
 0-.424-.085-.594.255-.085.511-.17.682-.254.51-.255 1.19-.765
 1.446-1.784.255-1.019-.17-1.781-.51-2.206-1.192-1.443-4.853-3.142-9.28-4.076C11.833.708
 9.62.453 7.748.453Zm.457 1.505c1.573.023 3.548.257 5.67.703 4.853
 1.103 8.514 2.887 8.259 4.075-.256 1.189-4.427
 1.273-9.195.255-4.852-1.104-8.513-2.887-8.258-4.076.144-.669
 1.501-.987 3.524-.957Zm-.287 5.797c1.362.425 2.895.934 4.513 1.273
 2.81.68 5.447.85 7.576.765 0 1.189-4 2.208-8.939 2.208-4.937
 0-8.938-1.02-8.938-2.208 0-.934 2.383-1.698 5.788-2.038zm-4.343
 5.519c1.958.51 4.513.849 7.408.849 2.894 0 5.447-.34
 7.406-.849.936.425 1.532.849 1.532 1.273 0 1.189-4 2.208-8.938
 2.208-4.938 0-8.94-1.02-8.94-2.208 0-.51.596-.933 1.532-1.273zm0
 4.754c1.958.51 4.513.85 7.408.85 2.894 0 5.447-.34 7.406-.85.936.425
 1.532.85 1.532 1.275 0 1.189-4 2.206-8.938 2.206-4.938
 0-8.94-1.017-8.94-2.206 0-.51.596-.935 1.532-1.275z" />
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
