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


class LenovoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lenovo"

    @property
    def original_file_name(self) -> "str":
        return "lenovo.svg"

    @property
    def title(self) -> "str":
        return "Lenovo"

    @property
    def primary_color(self) -> "str":
        return "#E2231A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lenovo</title>
     <path d="M21.044 12.288c0 .5-.343.867-.815.867-.464
 0-.827-.38-.827-.867 0-.51.343-.868.815-.868.464 0
 .827.381.827.868zm-14.305-.92a.787.787 0 0 0-.651.307.991.991 0 0
 0-.172.738l1.479-.614a.708.708 0 0 0-.656-.43zm6.963.052c-.472
 0-.816.358-.816.868 0 .486.364.867.828.867.472 0 .815-.368.815-.867
 0-.487-.363-.868-.827-.868zM24 7.997v8.006H0V7.997h24zM5.01
 13.05H3.088V9.825H2.23v4.003h2.78v-.777zm1.137-.094l2.163-.897a1.667
 1.667 0 0 0-.37-.86c-.284-.33-.704-.505-1.216-.505-.931
 0-1.633.686-1.633 1.593 0 .93.704 1.593 1.726 1.593.572 0 1.158-.272
 1.432-.589l-.535-.411c-.357.264-.56.326-.885.326-.292
 0-.52-.09-.682-.25zm5.57-1.039c0-.709-.507-1.223-1.252-1.223a1.28
 1.28 0 0
 0-1.005.494v-.442h-.846v3.081h.846v-1.753c0-.316.245-.651.698-.651.35
 0
 .712.243.712.651v1.753h.847v-1.91zm3.647.37c0-.904-.725-1.593-1.65-1.593-.933
 0-1.663.7-1.663 1.593 0 .903.726 1.592 1.651 1.592.932 0 1.662-.7
 1.662-1.592zm2.066 1.54l1.268-3.081h-.967l-.765
 2.099-.765-2.1h-.966l1.268
 3.081h.927zm4.449-1.54c0-.904-.725-1.593-1.65-1.593-.932
 0-1.662.7-1.662 1.593 0 .903.725 1.592 1.65 1.592.932 0 1.662-.7
 1.662-1.592z" />
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
