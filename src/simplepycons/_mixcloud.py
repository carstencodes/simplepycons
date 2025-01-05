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


class MixcloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mixcloud"

    @property
    def original_file_name(self) -> "str":
        return "mixcloud.svg"

    @property
    def title(self) -> "str":
        return "Mixcloud"

    @property
    def primary_color(self) -> "str":
        return "#5000FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mixcloud</title>
     <path d="M2.462 8.596l1.372
 6.49h.319l1.372-6.49h2.462v6.808H6.742v-5.68l.232-.81h-.402l-1.43
 6.49H2.854l-1.44-6.49h-.391l.222.81v5.68H0V8.596zM24
 8.63v1.429L21.257 12 24 13.941v1.43l-3.235-2.329h-.348l-3.226
 2.329v-1.43l2.734-1.94-2.733-1.942V8.63l3.225 2.338h.348zm-7.869
 2.75v1.24H9.304v-1.24z" />
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
