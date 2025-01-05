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


class OperaGxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "operagx"

    @property
    def original_file_name(self) -> "str":
        return "operagx.svg"

    @property
    def title(self) -> "str":
        return "Opera GX"

    @property
    def primary_color(self) -> "str":
        return "#EE2950"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Opera GX</title>
     <path d="M24 12.01c0 3.412-1.462 6.674-4.013 8.943A12 12 0 0 1
 11.992 24c-.178 0-.385-.019-.563-.019C5.016 23.681 0 18.403 0 11.991
 0 5.37 5.372 0 11.99 0h.038c2.944 0 5.775 1.087 7.96 3.047A12.04
 12.04 0 0 1 24 12.009zm-9.14
 10.443c-2.729-.056-5.279-1.397-7.041-3.684-1.388-1.64-2.203-4.013-2.269-6.516v-.544c.047-2.521.881-4.893
 2.269-6.534 1.744-2.269 4.294-3.61 7.012-3.666a10.67 10.67 0 0
 0-2.784-.384h-.038c-5.99 0-10.865 4.894-10.865 10.866 0 5.812 4.528
 10.584 10.34 10.847a10.087 10.087 0 0 0
 3.375-.385zm7.996-10.444c0-3.065-1.303-5.99-3.59-8.053a7.69 7.69 0 0
 0-4.228-1.284c-2.447 0-4.754 1.181-6.357 3.244-1.247 1.462-1.969
 3.59-2.025 5.83v.526c.056 2.25.778 4.369 2.006 5.812l.02.02c1.602
 2.071 3.909 3.252 6.355 3.252a7.69 7.69 0 0 0 4.229-1.284 10.894
 10.894 0 0 0 3.59-8.063zm-3.75 0c0 4.05-2.184 7.341-4.912 7.585
 2.128-1.388 3.61-4.257 3.61-7.585 0-3.328-1.463-6.197-3.61-7.575
 2.728.244 4.912 3.525 4.912 7.575z" />
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
