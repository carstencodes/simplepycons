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


class ImagejIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "imagej"

    @property
    def original_file_name(self) -> "str":
        return "imagej.svg"

    @property
    def title(self) -> "str":
        return "ImageJ"

    @property
    def primary_color(self) -> "str":
        return "#00D8E0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ImageJ</title>
     <path d="M13.1286 17.5084h-8.072a.187.187 0 0
 1-.187-.187v-.4442a.187.187 0 0 1 .187-.187h8.0721a.187.187 0 0 1
 .187.187v.4442a.1872.1872 0 0
 1-.1871.187zm5.6234-12.195c-1.4233.0033-4.2184-.0098-5.6414-.0065a.4035.4035
 0 0 0-.4035.4035v3.6061c0
 .2229.1807.4035.4035.4035h1.7475v8.19a1.8275 1.8275 0 0 1-.9112
 1.5761 1.8277 1.8277 0 0 1-1.8224 0 1.8276 1.8276 0 0
 1-.9113-1.5784H6.941c0 2.1705 1.1677 4.193 3.0473 5.2782.9398.5428
 1.9936.8141 3.0474.8141s2.1076-.2713 3.0474-.8139c1.8795-1.0837
 3.0444-3.1089 3.0473-5.274V5.692a.3785.3785 0 0 0-.3784-.3786zM7.4546
 15.2306h3.276a.6403.6403 0 0 0 .6403-.6403V.6403A.6403.6403 0 0 0
 10.7306 0h-3.276a.6403.6403 0 0 0-.6403.6403v13.95c0
 .3536.2867.6403.6403.6403z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/imagej/imagej/blob/0667395'''

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
