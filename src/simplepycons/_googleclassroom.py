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


class GoogleClassroomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleclassroom"

    @property
    def original_file_name(self) -> "str":
        return "googleclassroom.svg"

    @property
    def title(self) -> "str":
        return "Google Classroom"

    @property
    def primary_color(self) -> "str":
        return "#0F9D58"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Classroom</title>
     <path d="M1.6367 1.6367C.7322 1.6367 0 2.369 0 3.2734v17.4532c0
 .9045.7322 1.6367 1.6367 1.6367h20.7266c.9045 0 1.6367-.7322
 1.6367-1.6367V3.2734c0-.9045-.7322-1.6367-1.6367-1.6367H1.6367zm.545
 2.1817h19.6367v16.3632h-2.7266v-1.0898h-4.9102v1.0898h-12V3.8184zM12
 8.1816c-.9046 0-1.6367.7322-1.6367 1.6368 0 .9045.7321 1.6367 1.6367
 1.6367.9046 0 1.6367-.7322 1.6367-1.6367
 0-.9046-.7321-1.6368-1.6367-1.6368zm-4.3633 1.9102c-.6773
 0-1.2285.5493-1.2285 1.2266 0 .6772.5512 1.2265 1.2285 1.2265.6773 0
 1.2266-.5493 1.2266-1.2265 0-.6773-.5493-1.2266-1.2266-1.2266zm8.7266
 0c-.6773 0-1.2266.5493-1.2266 1.2266 0 .6772.5493 1.2265 1.2266
 1.2265.6773 0 1.2285-.5493 1.2285-1.2265
 0-.6773-.5512-1.2266-1.2285-1.2266zM12 12.5449c-1.179
 0-2.4128.4012-3.1484
 1.0059-.384-.1198-.8043-.1875-1.2149-.1875-1.3136 0-2.7285.695-2.7285
 1.5586v.8965h14.1836v-.8965c0-.8637-1.4149-1.5586-2.7285-1.5586-.4106
 0-.831.0677-1.2149.1875-.7356-.6047-1.9694-1.0059-3.1484-1.0059Z" />
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
