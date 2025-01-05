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


class YetiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yeti"

    @property
    def original_file_name(self) -> "str":
        return "yeti.svg"

    @property
    def title(self) -> "str":
        return "Yeti"

    @property
    def primary_color(self) -> "str":
        return "#00263C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yeti</title>
     <path d="M14.575
 8.582v1.685h2.183v5.15h2.14v-5.15h2.183V8.583h-6.505ZM0 8.582l2.699
 3.972v2.864h2.144v-2.864l2.693-3.971H5.172l-1.398
 2.305-1.397-2.305zm8.022
 0v6.836h5.84v-1.663h-3.694v-.974H13.3v-1.54h-3.132v-.974h3.589V8.583Zm13.832
 0 .001 6.836H24V8.583Z" />
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
