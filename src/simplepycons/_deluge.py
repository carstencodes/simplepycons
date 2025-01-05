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


class DelugeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deluge"

    @property
    def original_file_name(self) -> "str":
        return "deluge.svg"

    @property
    def title(self) -> "str":
        return "Deluge"

    @property
    def primary_color(self) -> "str":
        return "#094491"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deluge</title>
     <path d="M18.766 10.341 12.006 0l-6.77 10.342c-1.945 2.97-2.191
 6.432-.66 9.264C6.04 22.316 8.885 24 12.001 24c3.113 0 5.957-1.681
 7.421-4.388 1.532-2.832 1.287-6.297-.657-9.27zm-10.082 6.9c1.433
 2.554 3.608 3.045 6.585 2.102-1.7 1.848-5.188
 2.337-7.557-.302-1.63-1.817-1.773-4.351-.642-6.468 1.132-2.117
 3.388-2.706 5.012-1.551-3.723.09-4.43 4.38-3.398
 6.218zm8.72-6.009c.723 1.107 1.152 2.267 1.314 3.418-3.354
 5.763-7.862 4.879-9.062 1.377-.554-1.618 1.19-5.08
 4.514-3.725-1.296-2.838-4.238-4.017-6.911-1.809a5.099 5.099 0 0
 0-.609.66l5.355-8.179 5.398 8.258z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/deluge-torrent/deluge/blob
/0b5f45b486e8e974ba8a0b1d6e8edcd124fca62a/deluge/ui/data/pixmaps/delug'''

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
