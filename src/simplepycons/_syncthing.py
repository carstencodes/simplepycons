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


class SyncthingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "syncthing"

    @property
    def original_file_name(self) -> "str":
        return "syncthing.svg"

    @property
    def title(self) -> "str":
        return "Syncthing"

    @property
    def primary_color(self) -> "str":
        return "#0891D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Syncthing</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zm0 2.412c3.115 0 5.885 1.5 7.629 3.815a1.834
 1.834 0 0 1 1.564 3.162c.23.818.354 1.68.354 2.57a9.504 9.504 0 0
 1-2.166 6.05c.128.281.189.595.162.92a1.854 1.854 0 0 1-2.004 1.678
 1.86 1.86 0 0 1-.877-.322A9.486 9.486 0 0 1 12 21.505c-3.84
 0-7.154-2.277-8.668-5.552-.3-.01-.601-.092-.879-.254-.858-.51-1.144-1.634-.633-2.513.164-.276.39-.493.653-.643a9.62
 9.62 0 0 1-.02-.584c0-5.265 4.282-9.547 9.547-9.547zm0 1.227a8.311
 8.311 0 0 0-8.31
 8.683c.22.036.439.111.644.23.323.2.564.484.713.805l6.984-.644a1.78
 1.78 0 0 1
 .787-1.08c.288-.19.612-.286.936-.295.34-.01.68.08.978.254l3.51-2.914a1.82
 1.82 0 0 1 .317-1.84A8.3 8.3 0 0 0 12 3.638zm7.027 5.98-3.502
 2.91a1.829 1.829 0 0 1-.23 1.719l1.904
 2.744c.212-.06.436-.085.668-.066.238.024.46.092.66.193a8.285 8.285 0
 0 0 1.793-5.16 8.38 8.38 0 0 0-.265-2.092 1.835 1.835 0 0
 1-1.028-.248zm-6.886 4.315-6.975.644a1.8 1.8 0 0 1-.66 1.004A8.312
 8.312 0 0 0 12 20.279a8.294 8.294 0 0 0 3.938-.986 1.845 1.845 0 0
 1-.075-.69c.028-.341.148-.65.332-.908L14.29 14.95a1.839 1.839 0 0
 1-2.148-1.015z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/syncthing/syncthing/blob/b'''

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
