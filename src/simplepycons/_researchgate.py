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


class ResearchgateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "researchgate"

    @property
    def original_file_name(self) -> "str":
        return "researchgate.svg"

    @property
    def title(self) -> "str":
        return "ResearchGate"

    @property
    def primary_color(self) -> "str":
        return "#00CCBB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ResearchGate</title>
     <path d="M19.586 0c-.818
 0-1.508.19-2.073.565-.563.377-.97.936-1.213 1.68a3.193 3.193 0 0
 0-.112.437 8.365 8.365 0 0 0-.078.53 9 9 0 0
 0-.05.727c-.01.282-.013.621-.013 1.016a31.121 31.123 0 0 0 .014 1.017
 9 9 0 0 0 .05.727 7.946 7.946 0 0 0 .077.53h-.005a3.334 3.334 0 0 0
 .113.438c.245.743.65 1.303 1.214 1.68.565.376 1.256.564 2.075.564.8 0
 1.536-.213 2.105-.603.57-.39.94-.916
 1.175-1.65.076-.235.135-.558.177-.93a10.9 10.9 0 0 0
 .043-1.207v-.82c0-.095-.047-.142-.14-.142h-3.064c-.094
 0-.14.047-.14.141v.956c0 .094.046.14.14.14h1.666c.056 0
 .084.03.084.086 0 .36 0
 .62-.036.865-.038.244-.1.447-.147.606-.108.385-.348.664-.638.876-.29.212-.738.35-1.227.35-.545
 0-.901-.15-1.21-.353-.306-.203-.517-.454-.67-.915a3.136 3.136 0 0
 1-.147-.762 17.366 17.367 0 0
 1-.034-.656c-.01-.26-.014-.572-.014-.939a26.401 26.403 0 0 1
 .014-.938 15.821 15.822 0 0 1 .035-.656 3.19 3.19 0 0 1 .148-.76 1.89
 1.89 0 0 1 .742-1.01c.344-.244.593-.352 1.137-.352.508 0 .815.096
 1.144.303.33.207.528.492.764.925.047.094.111.118.198.07l1.044-.43c.075-.048.09-.115.042-.199a3.549
 3.549 0 0 0-.466-.742 3 3 0 0 0-.679-.607 3.313 3.313 0 0
 0-.903-.41A4.068 4.068 0 0 0 19.586 0zM8.217 5.836c-1.69
 0-3.036.086-4.297.086-1.146 0-2.291
 0-3.007-.029v.831l1.088.2c.744.144 1.174.488 1.174 2.264v11.288c0
 1.777-.43 2.12-1.174 2.263l-1.088.2v.832c.773-.029 2.12-.086
 3.465-.086 1.29 0 2.951.057
 3.667.086v-.831l-1.49-.2c-.773-.115-1.174-.487-1.174-2.264v-4.784c.688.057
 1.29.057 2.206.057 1.748 3.123 3.41 5.472 4.355 6.56.86 1.032 2.177
 1.691 3.839 1.691.487 0 1.003-.086 1.318-.23v-.744c-1.031
 0-2.063-.716-2.808-1.518-1.26-1.376-2.95-3.582-4.355-6.074 2.32-.545
 4.04-2.722 4.04-4.9 0-3.208-2.492-4.698-5.758-4.698zm-.515 1.29c2.406
 0 3.839 1.26 3.839 3.552 0 2.263-1.547 3.782-4.097 3.782-.974
 0-1.404-.03-2.063-.086v-7.19c.66-.059 1.547-.059 2.32-.059z" />
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
