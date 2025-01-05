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


class RecoilIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "recoil"

    @property
    def original_file_name(self) -> "str":
        return "recoil.svg"

    @property
    def title(self) -> "str":
        return "Recoil"

    @property
    def primary_color(self) -> "str":
        return "#3578E5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Recoil</title>
     <path d="M17.09 8.862a3.017 3.018 0 00-2.615-2.43l-.245-.03a1.662
 1.662 0 01-1.453-1.645v-.856a2.028 2.028 0 10-1.602-.02v.874a3.263
 3.264 0 002.855 3.236l.245.032c.764.096 1.144.66 1.246
 1.155.1.495-.03 1.163-.698 1.55a2.569 2.569 0
 01-1.055.337l-3.68.346a4.212 4.212 0 00-1.71.546 3.02 3.02 0 00-1.468
 3.257 3.017 3.018 0 002.615 2.43l.245.032a1.662 1.662 0 011.453
 1.644v.777a2.03 2.03 0 101.602.016v-.793a3.263 3.264 0
 00-2.856-3.236l-.244-.032c-.764-.096-1.145-.66-1.246-1.155-.1-.495.03-1.163.697-1.55a2.569
 2.569 0 011.057-.337l3.68-.345a4.212 4.212 0 001.71-.546 3.023 3.024
 0 001.467-3.258zm-2.653 4.708a5.71 5.71 0 01-.436.06l-1.543.147 1.93
 2.119a3.47 3.47 0 01.906 2.34H16.9a5.07 5.07 0
 00-1.325-3.42zm-5.003-3.11a4.65 4.65 0 01.546-.08l1.427-.136L9.469
 8.12a3.47 3.47 0 01-.905-2.34H6.963c0 1.267.47 2.483 1.324 3.42z" />
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
