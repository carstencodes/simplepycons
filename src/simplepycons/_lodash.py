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


class LodashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lodash"

    @property
    def original_file_name(self) -> "str":
        return "lodash.svg"

    @property
    def title(self) -> "str":
        return "Lodash"

    @property
    def primary_color(self) -> "str":
        return "#3492FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lodash</title>
     <path d="m0 20.253h24v2.542h-24zm18.061-15.041.223.031c1.933-.071
 3.885 1.006 4.882 2.674.844 1.566.976 3.458.712 5.187-.204
 1.657-1.149 3.234-2.644 4.027-2.177 1.139-5.085
 1.017-7.017-.59-1.994-1.942-2.461-5.136-1.444-7.678.711-2.207 3-3.661
 5.288-3.63zm.234 1.8h-.183c-1.424-.03-2.777.915-3.285 2.237-.732
 1.831-.732 4.17.691 5.695 1.17 1.434 3.458 1.597 4.882.438
 1.525-1.312 1.83-3.59
 1.322-5.451-.275-1.648-1.78-2.929-3.458-2.929zm-18.295-5.807h2.237v14.847h8.848v1.831h-11.085z"
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
        return '''https://github.com/lodash/lodash.com/blob/c8d'''

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
