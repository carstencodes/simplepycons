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


class AppimageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appimage"

    @property
    def original_file_name(self) -> "str":
        return "appimage.svg"

    @property
    def title(self) -> "str":
        return "AppImage"

    @property
    def primary_color(self) -> "str":
        return "#739FB9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AppImage</title>
     <path d="M1.64 0C.735 0 0 .736 0 1.64v20.72C0 23.265.736 24 1.64
 24h20.72c.904 0 1.64-.736 1.64-1.64V1.64C24 .735 23.264 0 22.36
 0Zm8.56 2.42h3.6v3.6h1.912L12 10.22l-3.713-4.2H10.2Zm1.331
 8.4h1.313c.103 0 .169.177.169.394v1.368c.417.096.81.266
 1.162.488l.975-.975c.153-.153.32-.223.394-.15l.918.919c.074.073.004.24-.15.393l-.975.975c.223.352.393.745.488
 1.163h1.369c.217 0 .394.065.394.169v1.312c0
 .104-.177.169-.394.169h-1.369a3.74 3.74 0 0 1-.487
 1.162l.974.975c.154.154.224.32.15.394l-.918.919c-.074.073-.24.003-.394-.15l-.975-.975a3.74
 3.74 0 0 1-1.163.487v1.37c0 .216-.065.393-.168.393H11.53c-.103
 0-.169-.177-.169-.394v-1.369a3.74 3.74 0 0
 1-1.162-.487l-.975.975c-.153.153-.32.223-.394.15l-.918-.919c-.074-.073-.004-.24.15-.394l.974-.975a3.74
 3.74 0 0 1-.487-1.162H7.181c-.217
 0-.393-.065-.393-.169v-1.312c0-.104.176-.17.393-.17H8.55a3.74 3.74 0
 0 1
 .487-1.162l-.974-.975c-.154-.153-.224-.32-.15-.393l.918-.92c.074-.072.24-.002.394.15l.975.976a3.74
 3.74 0 0 1 1.163-.488v-1.368c0-.217.065-.394.168-.394zm.656
 3.731c-.917 0-1.668.752-1.668 1.669s.751 1.669 1.669 1.669c.917 0
 1.668-.752 1.668-1.67 0-.916-.751-1.668-1.669-1.668z" />
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
