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


class MinioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "minio"

    @property
    def original_file_name(self) -> "str":
        return "minio.svg"

    @property
    def title(self) -> "str":
        return "MinIO"

    @property
    def primary_color(self) -> "str":
        return "#C72E49"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MinIO</title>
     <path d="M13.2072.006c-.6216-.0478-1.2.1943-1.6211.582a2.15 2.15
 0 0 0-.0938 3.0352l3.4082 3.5507a3.042 3.042 0 0 1-.664
 4.6875l-.463.2383V7.2853a15.4198 15.4198 0 0 0-8.0174
 10.4862v.0176l6.5487-3.3281v7.621L13.7794
 24V13.6817l.8965-.4629a4.4432 4.4432 0 0 0
 1.2207-7.0292l-3.371-3.5254a.7489.7489 0 0 1 .037-1.0547.7522.7522 0
 0 1 1.0567.0371l.4668.4863-.006.0059 4.0704 4.2441a.0566.0566 0 0 0
 .082 0 .06.06 0 0 0
 0-.0703l-3.1406-5.1425-.1484.1425.1484-.1445C14.4945.3926
 13.8287.0538 13.2072.006Zm-.9024 9.8652v2.9941l-4.1523 2.1484a13.9787
 13.9787 0 0 1 2.7676-3.9277 14.1784 14.1784 0 0 1 1.3847-1.2148z" />
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
