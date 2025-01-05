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


class WiresharkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wireshark"

    @property
    def original_file_name(self) -> "str":
        return "wireshark.svg"

    @property
    def title(self) -> "str":
        return "Wireshark"

    @property
    def primary_color(self) -> "str":
        return "#1679A7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wireshark</title>
     <path d="m2.95 0c-1.62 0-2.95 1.32-2.95 2.95v18.1c0 1.63 1.32
 2.95 2.95 2.95h18.1c1.62 0 2.95-1.32
 2.95-2.95v-18.1c-.00024-1.63-1.32-2.95-2.95-2.95zm0 1.09h18.1c1.04 0
 1.85.818 1.85 1.86v14h-5.27c-.335-.796-2.57-6.47.283-10.9a.516.517 0
 0 0-.443-.794c-5.24.0827-8.2 3.19-9.74 6.21-1.35 2.64-1.63 4.91-1.69
 5.53h-4.95v-14c0-1.04.817-1.86 1.85-1.86zm13.6 5.24c-2.62 5.24.248
 11.4.248 11.4a.516.517 0 0 0 .469.301h5.62v3.05c0 1.04-.817 1.86-1.85
 1.86h-18.1c-1.04 0-1.85-.818-1.85-1.86v-3.05h5.39a.516.517 0 0 0
 .514-.477s.226-2.8 1.66-5.62c1.34-2.62 3.67-5.17 7.91-5.57z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.com/wanduow/wireshark/-/blob/c'''

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
