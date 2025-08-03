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


class KeployIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keploy"

    @property
    def original_file_name(self) -> "str":
        return "keploy.svg"

    @property
    def title(self) -> "str":
        return "Keploy"

    @property
    def primary_color(self) -> "str":
        return "#FF914D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Keploy</title>
     <path d="M7.438 0C6.8952-.0029 6.3924.2006
 5.954.6725c-.6953.7482-.354 1.7371.5356 2.7936 2.751.6529 6.3299
 2.3982 9.4374 4.8783C14.4729 6.0506 10.37.0158 7.4381 0ZM4.2622
 3.5776c-1.304.0225-2.2213.4728-2.4983 1.4363C.7452 8.5564 13.576
 10.6173 13.576 10.6173c.269.0468.4741.2807.4741.5625 0
 .292-.22.5298-.5034.564-7.508-.303-8.8518 4.309-8.8518 4.309C3.2689
 20.6625 7.6858 24 7.6858 24c-2.1293-8.5433 7.0439-4.9774
 7.0439-4.9774 7.5638 2.5793 7.8292.526
 7.4649-1.0566-.0027-.0127-.0037-.0256-.0067-.0386C20.4495 9.987
 9.3782 3.4895 4.262 3.5776Zm14.3353
 10.5971c.2358-.0018.524.1173.7714.3406.396.3576.5366.8461.3148
 1.091-.222.2447-.723.1535-1.1193-.2035-.3954-.3573-.536-.8458-.3141-1.0906.0832-.0918.2058-.1364.3472-.1375z"
 />
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
