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


class MediapipeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mediapipe"

    @property
    def original_file_name(self) -> "str":
        return "mediapipe.svg"

    @property
    def title(self) -> "str":
        return "MediaPipe"

    @property
    def primary_color(self) -> "str":
        return "#0097A7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MediaPipe</title>
     <path d="M2.182 0C1 0 .037.94.002 2.114L0 2.182v6.545a2.182 2.182
 0 0 0 4.364 0V2.182A2.182 2.182 0 0 0 2.182 0Zm6.545 0c-1.182
 0-2.145.94-2.18 2.114l-.002.068v13.09a2.182 2.182 0 0 0 4.364
 0V2.183A2.182 2.182 0 0 0 8.727 0Zm6.546 0a2.182 2.182 0 0 0-2.182
 2.182 2.182 2.182 0 0 0 2.182 2.182 2.182 2.182 0 0 0
 2.182-2.182A2.182 2.182 0 0 0 15.273 0Zm6.545 0c-1.182
 0-2.145.94-2.18 2.114l-.002.068v19.636a2.182 2.182 0 0 0 4.364
 0V2.182A2.182 2.182 0 0 0 21.818 0Zm-6.545 6.545c-1.183
 0-2.145.94-2.181 2.114l-.001.068v13.091a2.182 2.182 0 0 0 4.364
 0V8.728a2.182 2.182 0 0 0-2.182-2.183zM2.182 13.091c-1.182
 0-2.145.94-2.18 2.114L0 15.273v6.545a2.182 2.182 0 0 0 4.364
 0v-6.545a2.182 2.182 0 0 0-2.182-2.182zm6.545 6.545a2.182 2.182 0 0
 0-2.182 2.182A2.182 2.182 0 0 0 8.727 24a2.182 2.182 0 0 0
 2.182-2.182 2.182 2.182 0 0 0-2.182-2.182Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developers.google.com/static/mediapip'''

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
