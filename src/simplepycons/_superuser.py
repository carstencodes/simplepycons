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


class SuperUserIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "superuser"

    @property
    def original_file_name(self) -> "str":
        return "superuser.svg"

    @property
    def title(self) -> "str":
        return "Super User"

    @property
    def primary_color(self) -> "str":
        return "#38A1CE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Super User</title>
     <path d="M2.523 0c-.223 0-.336.111-.336.28v23.439c0
 .196.113.252.336.252h5.594c.224 0
 .335-.084.307-.252v-1.483c0-.167-.14-.252-.363-.252H5.543c-.252
 0-.363-.083-.363-.279V2.293c0-.196.112-.307.42-.307h2.488c.224 0
 .336-.056.336-.252V.28C8.424.084 8.284 0 8.06 0H2.523zm8.8.02c-.224
 0-.364.083-.364.279v1.398c0 .196.112.28.336.28h.447c2.154 0 3.664
 1.706 3.664 3.412v4.42c0 1.37.98 2.517 2.518
 3.216.112.056.139.14.139.196 0 .056-.027.112-.14.14-1.677.616-2.517
 2.294-2.517 3.496v3.916c0 1.735-1.51 1.258-3.664 1.258h-.447c-.224
 0-.336.084-.336.28v1.398c0 .196.14.28.363.28h.56c3.609 0 6.516.335
 6.516-2.714v-4.082c0-1.426 1.008-2.295
 2.49-2.714.672-.196.95-.307.923-.56v-1.173c0-.447-.308-.477-.868-.644-1.51-.532-2.515-1.342-2.515-2.74V5.64c0-3.05-2.937-5.621-6.545-5.621h-.56zm.183
 8.396c-.336 0-.645.252-.645.588v1.342c0
 .307.281.588.645.588h1.482c.336 0
 .643-.253.643-.588V9.004c0-.308-.28-.588-.643-.588h-1.482Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://stackoverflow.com/legal/trademark-gui'''
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
