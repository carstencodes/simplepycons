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


class OpenjdkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openjdk"

    @property
    def original_file_name(self) -> "str":
        return "openjdk.svg"

    @property
    def title(self) -> "str":
        return "OpenJDK"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenJDK</title>
     <path d="M11.915 0 11.7.215C9.515 2.4 7.47 6.39 6.046
 10.483c-1.064 1.024-3.633 2.81-3.711 3.551-.093.87 1.746 2.611 1.55
 3.235-.198.625-1.304 1.408-1.014 1.939.1.188.823.011
 1.277-.491a13.389 13.389 0 0 0-.017 2.14c.076.906.27 1.668.643
 2.232.372.563.956.911 1.667.911.397 0 .727-.114
 1.024-.264.298-.149.571-.33.91-.5.68-.34 1.634-.666 3.53-.604
 1.903.062 2.872.39 3.559.704.687.314 1.15.664 1.925.664.767 0
 1.395-.336 1.807-.9.412-.563.631-1.33.72-2.24.06-.623.055-1.32
 0-2.066.454.45 1.117.604
 1.213.424.29-.53-.816-1.314-1.013-1.937-.198-.624 1.642-2.366
 1.549-3.236-.08-.748-2.707-2.568-3.748-3.586C16.428 6.374 14.308
 2.394 12.13.215zm.175 6.038a2.95 2.95 0 0 1 2.943 2.942 2.95 2.95 0 0
 1-2.943 2.943A2.95 2.95 0 0 1 9.148 8.98a2.95 2.95 0 0 1
 2.942-2.942zM8.685 7.983a3.515 3.515 0 0 0-.145.997c0 1.951 1.6 3.55
 3.55 3.55 1.95 0 3.55-1.598 3.55-3.55
 0-.329-.046-.648-.132-.951.334.095.64.208.915.336a42.699 42.699 0 0 1
 2.042 5.829c.678 2.545 1.01 4.92.846 6.607-.082.844-.29 1.51-.606
 1.94-.315.431-.713.651-1.315.651-.593
 0-.932-.27-1.673-.61-.741-.338-1.825-.694-3.792-.758-1.974-.064-3.073.293-3.821.669-.375.188-.659.373-.911.5s-.466.2-.752.2c-.53
 0-.876-.209-1.16-.64-.285-.43-.474-1.101-.545-1.948-.141-1.693.176-4.069.823-6.614a43.155
 43.155 0 0 1 1.934-5.783c.348-.167.749-.31 1.192-.425zm-3.382
 4.362a.216.216 0 0 1 .13.031c-.166.56-.323 1.116-.463 1.665a33.849
 33.849 0 0 0-.547 2.555 3.9 3.9 0 0
 0-.2-.39c-.58-1.012-.914-1.642-1.16-2.08.315-.24 1.679-1.755
 2.24-1.781zm13.394.01c.562.027 1.926 1.543 2.24 1.783-.246.438-.58
 1.068-1.16 2.08a4.428 4.428 0 0 0-.163.309 32.354 32.354 0 0
 0-.562-2.49 40.579 40.579 0 0 0-.482-1.652.216.216 0 0 1 .127-.03z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://hg.openjdk.java.net/duke/duke/file/ca'''

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
