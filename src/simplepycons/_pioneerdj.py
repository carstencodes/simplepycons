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


class PioneerDjIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pioneerdj"

    @property
    def original_file_name(self) -> "str":
        return "pioneerdj.svg"

    @property
    def title(self) -> "str":
        return "Pioneer DJ"

    @property
    def primary_color(self) -> "str":
        return "#1A1928"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pioneer DJ</title>
     <path d="M15.46 5.569c1.474 1.144 1.715 2.695 1.107 4.319-.565
 1.503-1.833 2.96-3.827 4.087-2.21 1.227-4.498 1.554-6.993
 1.554H0L4.212 4.308h5.051c2.548 0 4.7.1 6.197 1.26zm-3.112
 4.235c.33-.884.246-2.202-.34-2.906-.658-.782-1.673-.873-3.138-.873l-.716.016s-.616-.07-.866.49c-.153.35.064-.263-2.412
 6.341-.326.876.452.919.452.919s2.794.17 5.132-1.448c.991-.685
 1.577-1.705 1.888-2.539zm5.938-1.467L24 8.366l-2.892 7.731c-.944
 2.518-2.896 3.595-6.812 3.595l-3.058-.04.731-1.746c4.427.21
 5.225-1.76 5.365-2.139l1.846-4.966s.317-.884-.402-.884h-1.132Z" />
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
