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


class AirplayVideoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airplayvideo"

    @property
    def original_file_name(self) -> "str":
        return "airplayvideo.svg"

    @property
    def title(self) -> "str":
        return "AirPlay Video"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AirPlay Video</title>
     <path d="M3.412 1.32c-1.178 0-1.584.122-2.031.366A2.449 2.449 0
 00.365 2.7C.122 3.148 0 3.553 0 4.771v9.137c0 1.178.122 1.585.365
 2.031.244.447.57.772 1.016 1.016.406.244.813.365
 2.031.365h2.72l1.138-1.34H3.006c-.325.041-.69-.001-1.016-.164-.203-.08-.366-.283-.488-.486-.122-.325-.203-.65-.162-1.016V4.406c-.04-.325
 0-.69.162-1.015.081-.203.285-.365.488-.487.325-.122.65-.204
 1.016-.164h17.867c.325-.04.69.002
 1.016.164.203.082.364.284.486.487.122.324.203.65.162
 1.015v9.95c.04.324 0 .69-.162
 1.015-.081.203-.283.365-.486.486-.325.122-.65.203-1.016.163h-4.264l1.137
 1.341 2.803-.04c1.218 0 1.623-.122 2.07-.366a2.449 2.449 0
 001.016-1.016c.243-.406.365-.813.365-2.03V4.77c0-1.218-.122-1.623-.365-2.07a2.449
 2.449 0 00-1.016-1.015c-.447-.244-.852-.366-2.07-.366H3.412zm8.451
 12.198a.501.501 0 00-.37.187l-7.106 8.162a.465.465 0
 00-.123.326.47.47 0 00.488.487h14.293c.122 0
 .245-.04.326-.121.203-.163.204-.489.041-.692l-7.107-8.162-.041-.04a.594.594
 0 00-.4-.147z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.apple.com/legal/intellectual-prop'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developer.apple.com/design/human-inte'''

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
