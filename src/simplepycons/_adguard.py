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


class AdguardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adguard"

    @property
    def original_file_name(self) -> "str":
        return "adguard.svg"

    @property
    def title(self) -> "str":
        return "AdGuard"

    @property
    def primary_color(self) -> "str":
        return "#68BC71"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AdGuard</title>
     <path d="M12 0C8.249 0 3.725.861 0 2.755 0 6.845-.051 17.037 12
 24 24.051 17.037 24 6.845 24 2.755 20.275.861 15.751 0 12 0zm-.106
 15.429L6.857 9.612c.331-.239 1.75-1.143 2.794.042l2.187
 2.588c.009-.001 5.801-5.948 5.815-5.938.246-.22.694-.503
 1.204-.101l-6.963 9.226z" />
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
