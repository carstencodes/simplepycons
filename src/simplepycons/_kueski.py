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


class KueskiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kueski"

    @property
    def original_file_name(self) -> "str":
        return "kueski.svg"

    @property
    def title(self) -> "str":
        return "Kueski"

    @property
    def primary_color(self) -> "str":
        return "#0075FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kueski</title>
     <path d="M19.403 7.989h-4.142c.029-1.022.506-1.33
 1.48-1.95l2.294-1.47a2.161 2.161 0 0 0
 1.048-1.776V.609c0-.62-.45-.787-1.038-.407l-3.043
 1.962c-1.088.706-1.72 1.493-2.007
 2.463-.194-1.02-.982-1.976-1.977-2.478L9.007.643C8.416.357 7.966.43
 7.96 1.046L7.954 3.23a1.88 1.88 0 0 0 1.038 1.668l2.263 1.12c.933.47
 1.47.648 1.491 1.97H4.592a.67.67 0 0 0-.674.667v2.665a.679.679 0 0 0
 .2.472.67.67 0 0 0 .474.193h14.811a.67.67 0 0 0
 .678-.665V8.655a.663.663 0 0 0-.2-.474.67.67 0 0 0-.478-.192zm0
 0h-4.142c.029-1.022.506-1.33 1.48-1.95l2.294-1.47a2.161 2.161 0 0 0
 1.048-1.776V.609c0-.62-.45-.787-1.038-.407l-3.043
 1.962c-1.088.706-1.72 1.493-2.007
 2.463-.194-1.02-.982-1.976-1.977-2.478L9.007.643C8.416.357 7.966.43
 7.96 1.046L7.954 3.23a1.88 1.88 0 0 0 1.038 1.668l2.263 1.12c.933.47
 1.47.648 1.491 1.97H4.592a.67.67 0 0 0-.674.667v2.665a.679.679 0 0 0
 .2.472.67.67 0 0 0 .474.193h14.811a.67.67 0 0 0
 .678-.665V8.655a.663.663 0 0 0-.2-.474.67.67 0 0 0-.478-.192zm-.007
 5.903c0 .343-.657 6.288-.968
 9.195-.09.857-.955.913-1.188.913H7.244c-1.04
 0-1.411-.456-1.512-1-.106-.572-.658-6.161-.934-8.108l-.096-.967c0-.482.339-.896.81-.896h13.021a.867.867
 0 0 1 .8.537.854.854 0 0 1 .063.332z" />
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
