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


class KucoinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kucoin"

    @property
    def original_file_name(self) -> "str":
        return "kucoin.svg"

    @property
    def title(self) -> "str":
        return "KuCoin"

    @property
    def primary_color(self) -> "str":
        return "#01BC8D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KuCoin</title>
     <path d="m7.928 11.996 7.122 7.122 4.49-4.49a2.004 2.004 0 0 1
 2.865 0 2.004 2.004 0 0 1 0 2.865l-5.918 5.918a2.058 2.058 0 0
 1-2.883 0l-8.541-8.542v5.07a2.034 2.034 0 1 1-4.07 0V4.043a2.034
 2.034 0 1 1 4.07 0v5.088L13.604.589a2.058 2.058 0 0 1 2.883 0l5.918
 5.918c.785.803.785 2.088 0 2.865-.804.785-2.089.785-2.865
 0l-4.49-4.49zM15.05 9.96a2.038 2.038 0 0 0-2.053 2.035c0 1.133.902
 2.052 2.035 2.052a2.038 2.038 0 0 0 2.053-2.035v-.018a2.07 2.07 0 0
 0-2.035-2.034z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.kucoin.com/news/en-kucoin-media-k'''

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
