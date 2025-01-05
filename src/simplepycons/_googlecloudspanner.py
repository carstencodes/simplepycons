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


class GoogleCloudSpannerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecloudspanner"

    @property
    def original_file_name(self) -> "str":
        return "googlecloudspanner.svg"

    @property
    def title(self) -> "str":
        return "Google Cloud Spanner"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Cloud Spanner</title>
     <path d="M12 9.06 7.944 6.864V2.388L10.38.924v3.66l1.62.744
 1.62-.744V.924l2.436 1.464v4.476L12 9.06zm-8.124 4.752L0
 16.056v2.988l3.228-1.86 1.404.912.096 1.632-3.24 1.872 2.616 1.476
 3.828-2.268-.132-4.596-3.924-2.4zm9.732-.9V8.758l-1.37.742-.238.129-.238-.13-1.37-.741v4.154l-3.613
 2.09 1.282.783.231.142.008.27.046 1.612L12 15.696l3.595
 2.079.045-1.59.008-.27.231-.142 1.301-.795-3.572-2.066zm7.164
 4.272L24 19.044v-2.988L20.064 13.8l-3.924 2.4-.132 4.596 3.888 2.244
 2.616-1.44-3.24-1.836.096-1.668 1.404-.912z" />
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
