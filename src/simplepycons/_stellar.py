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


class StellarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stellar"

    @property
    def original_file_name(self) -> "str":
        return "stellar.svg"

    @property
    def title(self) -> "str":
        return "Stellar"

    @property
    def primary_color(self) -> "str":
        return "#FDDA24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stellar</title>
     <path d="M12.003 1.716c-1.37 0-2.7.27-3.948.78A10.18 10.18 0 0 0
 2.66 7.901a10.136 10.136 0 0 0-.797 3.954c0 .258.01.516.027.775a1.942
 1.942 0 0 1-1.055 1.88L0
 14.934v1.902l2.463-1.26.072-.032v.005l.77-.39.758-.385.066-.039
 14.807-7.56 1.666-.847 3.392-1.732V2.694L17.792 5.86 3.744
 13.025l-.104.055-.017-.115a8.286 8.286 0 0
 1-.071-1.105c0-2.255.88-4.377 2.474-5.977a8.462 8.462 0 0 1 2.71-1.82
 8.513 8.513 0 0 1 3.2-.654h.067a8.41 8.41 0 0 1 4.09
 1.055l1.628-.83.126-.066a10.11 10.11 0 0 0-5.845-1.853zM24 7.143
 5.047 16.808l-1.666.847L0 19.382v1.902l3.282-1.671 2.91-1.485
 14.058-7.153.105-.055.016.115c.05.369.072.743.072 1.11 0 2.255-.88
 4.383-2.475 5.978a8.461 8.461 0 0 1-2.71 1.82 8.305 8.305 0 0
 1-3.2.654h-.06c-1.441
 0-2.86-.369-4.102-1.061l-.066.033-1.683.857c.594.418 1.232.776 1.903
 1.062a10.11 10.11 0 0 0 3.947.797 10.09 10.09 0 0 0 7.17-2.975 10.136
 10.136 0 0 0 2.969-7.18c0-.259-.005-.523-.027-.781a1.942 1.942 0 0 1
 1.055-1.88L24 9.044z" />
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
